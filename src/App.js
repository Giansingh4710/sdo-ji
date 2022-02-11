import React from "react";
import "./App.css";
import { Bookmark, BookmarkOutline } from "react-ionicons";

import { TRACK_NAMES, TRACK_LINKS } from "./TRACKS";

function App() {
  const [trackIndex, setTrackIndex] = React.useState(-1);

  return (
    <div className="App">
      <h1>Bhai Mohinder Singh Ji SDO</h1>
      <ShowRandTrack trackIndex={trackIndex} />
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
//const TEST = (savedTracks,trackIndex) => {
  //console.log("In state");
  //return savedTracks.includes(trackIndex);
//};

function ShowRandTrack({ trackIndex }) {
  let savedTracks = localStorage.getItem("savedTracks");
  if (savedTracks === null) {
    savedTracks = JSON.stringify([]);
  }
  savedTracks = JSON.parse(savedTracks);
  console.log(savedTracks, trackIndex, savedTracks.includes(trackIndex));

  const [trackSaved, setTrackSaved] = React.useState(savedTracks.includes(trackIndex));
  console.log(trackSaved);

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
      {trackSaved ? (
        <Bookmark
          onClick={() => {
            console.log("hii");
            setTrackSaved(false);
          }}
        />
      ) : (
        <BookmarkOutline
          onClick={() => {
            console.log("BYEE");
            setTrackSaved(true);
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
