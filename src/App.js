import React from "react";
import "./App.css";

import { TRACK_NAMES, TRACK_LINKS } from "./TRACKS";

function App() {
  const [trackIndex, setTrackIndex] = React.useState(-1);
  //for searching
  const [searchWord, setSearchWord] = React.useState("");
  const [showSearchedTracks, setShowSearchedTracks] = React.useState("");

  const trackNamesWithNums = TRACK_NAMES.map((elem, ind) => {
    const withNum = ind + 1 + ") " + elem.toLowerCase();
    return withNum;
  });

  const showRandTrack = () => {
    if (trackIndex === -1) {
      return;
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
      </div>
    );
  };

  const updateSearchedTracks = (theWord) => {
    if (theWord === null) return;
    const allTracksWithWord = trackNamesWithNums.filter((title) =>
      title.includes(theWord.toLowerCase())
    );

    if (allTracksWithWord.length === 0) {
      setShowSearchedTracks("'" + theWord + "' not in any of the tracks");
      return;
    }
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
  };
  return (
    <div className="forSearch">
      <div className="App">
        <h1>Bhai Mohinder Singh Ji SDO</h1>
        {showRandTrack()}
        <button
          onClick={() => {
            const randNum = Math.floor(Math.random() * 361); //in total there are 360 tracks
            setTrackIndex(randNum);
          }}
        >
          Play Random Keertan Track
        </button>

        <h2>Search for Track:</h2>
        <form onSubmit={(e) => e.preventDefault()}>
          <input
            autoFocus="autofocus"
            placeholder="Bin Ek Naam"
            value={searchWord}
            onChange={(e) => {
              setSearchWord(e.target.value);
            }}
          />
          <button
            type="submit"
            onClick={() => {
              updateSearchedTracks(searchWord);
            }}
          >
            Submit
          </button>
        </form>
      </div>
      {showSearchedTracks}
    </div>
  );
}

export default App;
