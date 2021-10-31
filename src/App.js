import React from "react";
import "./App.css";

import { TRACK_NAMES, TRACK_LINKS } from "./TRACKS";

function App() {
  const [trackIndex, setTrackIndex] = React.useState(-1);

  function showTrack() {
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
  }
  return (
    <div className="App">
      <h1>Bhai Mohinder Singh Ji SDO</h1>
      {showTrack()}
      <button
        onClick={() => {
          const randNum = Math.floor(Math.random() * 361); //in total there are 360 tracks
          // console.log(randNum);
          setTrackIndex(randNum);
        }}
      >
        Play Random Keertan Track
      </button>
    </div>
  );
}

export default App;
