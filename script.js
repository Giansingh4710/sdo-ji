// let isChromium = !!window.chrome;
let isChromium = false;


const tracksPlayed = [];
let currentTrackPointer = -1;
const keertani = document.getElementById("MainTitle").innerText;

function playNextTrack() {
  document.getElementById("playNext").innerHTML = "Next &rarr;";
  if (tracksPlayed.length - 1 == currentTrackPointer) {
    playRandTrack();
    return;
  }
  currentTrackPointer += 1;
  playTrack(tracksPlayed[currentTrackPointer]);
}

function playPreviousTrack() {
  if (currentTrackPointer < 1) {
    return;
  }
  currentTrackPointer -= 1;
  playTrack(tracksPlayed[currentTrackPointer]);
}

function playRandTrack() {
  const randNum = Math.floor(Math.random() * TRACK_LINKS.length);
  tracksPlayed.push(randNum);
  currentTrackPointer += 1;
  playTrack(randNum);
}

function playTrack(trkInd, pushToLst = false, showMsg = false) {
  const h4 = document.getElementById("trackMsg");
  h4.innerText = "";
  if (pushToLst) {
    tracksPlayed.push(trkInd);
    currentTrackPointer = tracksPlayed.length - 1;
    if (showMsg) {
      h4.innerText = showMsg;
    }
  }

  function activateModal() {
    let modal = document.getElementById("myModal");

    // Get the button that opens the modal
    let btn = document.getElementById("saveTrackBtn");

    // Get the <span> element that closes the modal
    let span = document.getElementsByClassName("close")[0];

    // When the user clicks the button, open the modal
    btn.onclick = function() {
      modal.style.display = "block";
    };

    // When the user clicks on <span> (x), close the modal
    span.onclick = function() {
      modal.style.display = "none";
    };

    // When the user clicks anywhere outside of the modal, close it
    window.onclick = function(event) {
      if (event.target == modal) {
        modal.style.display = "none";
      }
    };
  }

  const trackPlaying = document.getElementById("trackPlaying");
  const theNameOfTrack = TRACK_NAMES[trkInd];
  const theLinkOfTrack = TRACK_LINKS[trkInd];
  trackPlaying.innerHTML = `
    <h3>
        <a 
          href=${theLinkOfTrack.replaceAll(" ", "%20")} 
          target="_blank"
          rel="noopener noreferrer"
        >
            ${theNameOfTrack}
        </a>
    </h3>`
  if (isChromium){
    // for some reason some files didn't play with audio tag in Chromium browsers
    trackPlaying.innerHTML += `
      <video onended="playNextTrack()" onerror="" controls autoPlay={true} src='${theLinkOfTrack}' >
        your browers doesn't support this file or the the file is corrupted
      </video>
      <button id="saveTrackBtn"> SAVE </button> `;
  }else{
    trackPlaying.innerHTML += `
      <audio onended="playNextTrack()" onerror="" controls autoPlay={true} src='${theLinkOfTrack}' >
        your browers doesn't support this file or the the file is corrupted
      </audio>
      <button id="saveTrackBtn"> SAVE </button> `;
  }
  activateModal();
  if ('mediaSession' in navigator) {
    navigator.mediaSession.metadata = new MediaMetadata({
      title: theNameOfTrack,
      artist: keertani,
      album: 'Vaheguru Jio'
    })
  }
}
navigator.mediaSession.setActionHandler('previoustrack', playPreviousTrack)
navigator.mediaSession.setActionHandler('nexttrack', playNextTrack)

function saveTrack() {
  const note = document.getElementById("noteForSavedTrack");
  putTrackInLocalStorage(tracksPlayed[currentTrackPointer], note.value);
  note.value = "";
  let modal = document.getElementById("myModal");
  modal.style.display = "none";
}

function deleteSavedTrack(trkInd) {
  const keertani = document.getElementById("MainTitle").innerText;
  let savedTracks = localStorage.getItem(keertani);
  savedTracks = JSON.parse(savedTracks);
  delete savedTracks[trkInd];
  localStorage.setItem(keertani, JSON.stringify(savedTracks));
  toggleSavedTracks();
  toggleSavedTracks();
}

function putTrackInLocalStorage(trackInd, note) {
  let savedTracks = localStorage.getItem(keertani);
  if (!savedTracks) {
    savedTracks = {};
  } else {
    savedTracks = JSON.parse(savedTracks);
  }
  savedTracks[trackInd] = note;
  localStorage.setItem(keertani, JSON.stringify(savedTracks));
}

const trackNamesWithNums = TRACK_NAMES.map((elem, ind) => {
  const withNum = ind + 1 + ") " + elem.toLowerCase();
  return withNum;
});

function searchForShabad(e) {
  const searchVal = e;
  const ol = document.getElementById("searchResults");

  const allTracksWithWord = trackNamesWithNums.filter((title) =>
    title.includes(searchVal.toLowerCase())
  );

  ol.innerHTML = "";
  if (searchVal === "") return;
  for (let track of allTracksWithWord) {
    const theNameOfTrack = track;
    const theTrackInd = parseInt(track.split(") ")[0]) - 1;
    li = document.createElement("li");
    li.innerHTML = `<button onclick="playTrack(${theTrackInd},true)">${theNameOfTrack}</button>`;
    ol.appendChild(li);
  }
}

function toggleSavedTracks() {
  const ol = document.getElementById("savedShabads");
  if (ol.innerHTML !== "") {
    ol.innerHTML = "";
    return;
  }

  const keertani = document.getElementById("MainTitle").innerText;
  let savedTracks = localStorage.getItem(keertani);
  savedTracks = JSON.parse(savedTracks);

  function transferOldSaved() {
    const oldTitle =
      "All keertanis (SDO Ji,Bhai HPS Ji,Giani Amolak Singh Ji, Bhai Jeevan Singh Ji)";
    console.log("checked if need to tranfer");
    if (!localStorage[oldTitle]) return;
    console.log("transfering....");

    let _savedTracks = localStorage.getItem(oldTitle);
    _savedTracks = JSON.parse(_savedTracks);

    for (const theTrackInd in _savedTracks) {
      const trkMsg = _savedTracks[theTrackInd].replace("\n", " ");
      putTrackInLocalStorage(theTrackInd, trkMsg);
    }
    delete localStorage[oldTitle];
  }

  transferOldSaved();
  for (const theTrackInd in savedTracks) {
    const theNameOfTrack = TRACK_NAMES[theTrackInd];
    const trkMsg = savedTracks[theTrackInd].replace("\n", " ");
    li = document.createElement("li");
    li.innerHTML = `
<button onclick="playTrack(${theTrackInd},true,'${trkMsg}')" > ${theNameOfTrack}</button> 
<button onclick="deleteSavedTrack(${theTrackInd})" >DELETE</button>
<p>${trkMsg}</p>
`;
    ol.appendChild(li);
    console.log(theNameOfTrack, ": ", trkMsg);
  }
}

