import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";

// ✅ Import components (paths MUST be correct)
import Homepage from "./components/Homepage";
import Dashboard from "./components/Dashboard";
import AnalyzeText from "./components/AnalyzeText";
import Stylometry from "./components/Stylometry";
import DatasetInsights from "./components/DatasetInsights";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Homepage />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/analyze" element={<AnalyzeText />} />
        <Route path="/stylometry" element={<Stylometry />} />
        <Route path="/dataset" element={<DatasetInsights />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
