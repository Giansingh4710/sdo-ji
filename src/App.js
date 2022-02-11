import React from "react";
import "./App.css";
import { Bookmark, BookmarkOutline } from "react-ionicons";

import { TRACK_NAMES, TRACK_LINKS } from "./TRACKS";

function App() {
  const [trackIndex, setTrackIndex] = React.useState(-1);

  let savedTracks = localStorage.getItem("savedTracks");
  if (savedTracks === null) {
    savedTracks = JSON.stringify([]);
  }
  savedTracks = JSON.parse(savedTracks);
  const [trackSaved, setTrackSaved] = React.useState(
    savedTracks.includes(trackIndex)
  );
  console.log("FROM Main",savedTracks, trackSaved);
  return (
    <div className="App">
      <h1>Bhai Mohinder Singh Ji SDO</h1>
      <ShowRandTrack
        trackIndex={trackIndex}
        //trackSaved={savedTracks.includes(trackIndex)}
        savedTracks={savedTracks}
        //savedTracks={savedTracks}
      />
      <button
        autoFocus="autofocus"
        onClick={() => {
          const randNum = Math.floor(Math.random() * 361); //in total there are 360 tracks
          setTrackIndex(randNum);
        }}
      >
        Play Random Keertan Track
      </button>
      <SearchForTracks />
    </div>
  );
}

function ShowRandTrack({ trackIndex, savedTracks}) {
  //console.log(savedTracks.includes(trackIndex));
  console.log("Comp Rand", savedTracks.includes(trackIndex));
  if (trackIndex === -1) {
    return <div />;
  }

  const theNameOfTrack = TRACK_NAMES[trackIndex];
  const theLinkOfTrack = TRACK_LINKS[trackIndex];
  return (
    <div>
      <h3>{theNameOfTrack}</h3>
      <h5>
        <a href={theLinkOfTrack} target="_blank" rel="noopener noreferrer">
          Link To Keertan Track
        </a>
      </h5>
      <video
        controls
        autoPlay={true}
        name="media"
        loop
        src={theLinkOfTrack}
      ></video>
      {savedTracks.includes(trackIndex) ? (
        <Bookmark
          onClick={() => {
            console.log("hii");
            savedTracks=savedTracks.filter(item=>item!==trackIndex);
            console.log(savedTracks)
          }}
        />
      ) : (
        <BookmarkOutline
          onClick={() => {
            console.log("BYEE");
            savedTracks.push(trackIndex);
            console.log(savedTracks)
          }}
        />
      )}
    </div>
  );
}

function SearchForTracks() {
  const [searchWord, setSearchWord] = React.useState("");
  const [showSearchedTracks, setShowSearchedTracks] = React.useState("");

  const trackNamesWithNums = TRACK_NAMES.map((elem, ind) => {
    const withNum = ind + 1 + ") " + elem.toLowerCase();
    return withNum;
  });

  function updateSearchedTracks(wordInInput) {
    if (wordInInput === "") {
      setShowSearchedTracks("");
      return;
    }
    const allTracksWithWord = trackNamesWithNums.filter((title) =>
      title.includes(wordInInput.toLowerCase())
    );
    setShowSearchedTracks(
      <ol>
        {allTracksWithWord.map((elem) => {
          const theNameOfTrack = elem;
          const theLinkOfTrack = TRACK_LINKS[parseInt(elem.split(") ")[0]) - 1];
          return (
            <li key={elem}>
              <a
                href={theLinkOfTrack}
                target="_blank"
                rel="noopener noreferrer"
              >
                {theNameOfTrack}
              </a>
            </li>
          );
        })}
      </ol>
    );
    if (allTracksWithWord.length === 0) {
      setShowSearchedTracks(<p>{wordInInput} not in any of the tracks</p>);
    }
  }

  return (
    <div className="forSearch">
      <form onSubmit={(e) => e.preventDefault()}>
        <h2>Search for Track:</h2>
        <input
          placeholder="Bin Ek Naam"
          value={searchWord}
          onChange={(e) => {
            setSearchWord(e.target.value);
            updateSearchedTracks(e.target.value);
          }}
        />
        {showSearchedTracks}
      </form>
    </div>
  );
}

export default App;
