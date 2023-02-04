const tracksPlayed = [];
let currentTrackPointer = -1;
const keertani = document.getElementById("MainTitle").innerText;
playTrackFromLastTime()

navigator.mediaSession.setActionHandler('previoustrack', () => playPreviousTrack())
navigator.mediaSession.setActionHandler('nexttrack', () => playNextTrack())
navigator.mediaSession.setActionHandler('play', () => {
  const theAudioPlayer = document.getElementsByTagName('audio')[0]
  console.log("Played");
  theAudioPlayer.play()
})
navigator.mediaSession.setActionHandler('pause', () => {
  const theAudioPlayer = document.getElementsByTagName('audio')[0]
  console.log("Paused");
  theAudioPlayer.pause()
})

function playNextTrack() {
  if (tracksPlayed.length - 1 == currentTrackPointer) {
    if (tracksPlayed.length === 0)
      playRandTrack()
    else
      playTrack(tracksPlayed[currentTrackPointer]+1,true);
    return;
  }
  currentTrackPointer += 1;
  playTrack(tracksPlayed[currentTrackPointer]);
}

function playPreviousTrack() {
  if (currentTrackPointer < 1) {
    const newTrkInd = tracksPlayed[currentTrackPointer]-1;
    tracksPlayed.unshift(newTrkInd);
    playTrack(newTrkInd);
    return;
  }
  currentTrackPointer -= 1;
  playTrack(tracksPlayed[currentTrackPointer]);
}

function playRandTrack() {
  const randNum = Math.floor(Math.random() * TRACK_LINKS.length);
  tracksPlayed.push(randNum);
  currentTrackPointer = tracksPlayed.length - 1;
  playTrack(randNum);
}

function playTrack(trkInd, pushToLst = false, showMsg = false) {
  console.log(tracksPlayed,currentTrackPointer)
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
    let btn = document.getElementById("saveTrackBtn");
    let span = document.getElementsByClassName("close")[0];
    btn.onclick = function() { modal.style.display = "block"; };
    span.onclick = function() { modal.style.display = "none"; };
    window.onclick = function(event) {
      if (event.target == modal) { modal.style.display = "none"; }
    };
  }

  const theNameOfTrack = getNameOfTrack(TRACK_LINKS[trkInd]);
  const theLinkOfTrack = TRACK_LINKS[trkInd];

  const aTag = document.getElementById("trackNameAtag");
  const audioTag = document.getElementsByTagName("audio")[0];

  aTag.innerText = theNameOfTrack;
  aTag.href = theLinkOfTrack;
  audioTag.src = theLinkOfTrack

  document.getElementById("trackPlaying").style.display = "block"

  activateModal();
  if ('mediaSession' in navigator) {
    navigator.mediaSession.metadata = new MediaMetadata({
      title: theNameOfTrack,
      artist: keertani,
      album: 'Vaheguru Jio'
    })
  }
  localStorage.setItem("LastPlayed: " + keertani, trkInd)
}

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

function searchForShabad(e) {
  const searchVal = e;
  const ol = document.getElementById("searchResults");

  const allLinksWithWord = [];

  const searchWordsLst = searchVal.toLowerCase().split(' ')
  TRACK_LINKS.forEach((link, index) => {
    /* const trackName = getNameOfTrack(link) */
    const trackName = link.toLowerCase()
    let allWordsInTrackName = true
    for(const word of searchWordsLst){
      if (!trackName.includes(word)){
        allWordsInTrackName = false;
        break
      }
    }
    if(allWordsInTrackName){
      allLinksWithWord.push(index);
    }
  });

  ol.innerHTML = `<p>${allLinksWithWord.length} Results Found</p>`;
  if (searchVal === "") return;
  for (const index of allLinksWithWord) {
    li = document.createElement("li");
    li.innerHTML = `<button onclick="playTrack(${index},true)">${getNameOfTrack(TRACK_LINKS[index])}</button>`;
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

  for (const theTrackInd in savedTracks) {
    const theNameOfTrack = getNameOfTrack(TRACK_LINKS[theTrackInd])
    const trkMsg = savedTracks[theTrackInd].replace("\n", " ");
    li = document.createElement("li");
    li.innerHTML = `
      <button onclick="playTrack(${theTrackInd},true,'${trkMsg}')" > ${theNameOfTrack}</button> 
      <button onclick="deleteSavedTrack(${theTrackInd})" >DELETE</button>
      <p>${trkMsg}</p>`;
    ol.appendChild(li);
    console.log(theNameOfTrack, ": ", trkMsg);
  }
}

function playTrackFromLastTime() {
  const trackInd = parseInt(localStorage.getItem("LastPlayed: " + keertani));
  if (trackInd)
    playTrack(trackInd, true);
  else
    console.log("Could not get link from last session!")
}

function getNameOfTrack(link) { return link.split('/').slice(-1)[0] }
