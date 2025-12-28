import React, { useState } from "react";
import "./AnalyzeText.css";

function AnalyzeText() {
  const [text, setText] = useState("");

  return (
    <div className="page-container">
      <h2>Analyze Text</h2>

      <textarea
        placeholder="Enter text to analyze..."
        value={text}
        onChange={(e) => setText(e.target.value)}
      />

      <button>Analyze</button>

      <p className="note">
        This module performs offensive text classification and word-level tagging.
      </p>
    </div>
  );
}

export default AnalyzeText;
