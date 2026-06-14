import { Routes, Route } from "react-router-dom";
import Layout from "./components/Layout";
import HomePage from "./pages/HomePage";
import PodcastPage from "./pages/PodcastPage";
import EpisodePage from "./pages/EpisodePage";

export default function App() {
  return (
    <Routes>
      <Route element={<Layout />}>
        <Route index element={<HomePage />} />
        <Route path="podcast/:podcastId" element={<PodcastPage />} />
        <Route path="podcast/:podcastId/:episodeId" element={<EpisodePage />} />
      </Route>
    </Routes>
  );
}
