import { useState, useEffect } from "react";
import HomePage from "./pages/HomePage";
import GalleryPage from "./pages/GalleryPage";
import AboutPage from "./pages/AboutPage";
import DetailPage from "./pages/DetailPage";
import ErrorPage from "./pages/ErrorPage";
import PageHeader from "./components/PageHeader";
import PageFooter from "./components/PageFooter";
import "./App.css";

export default function App() {
  const [page, setPage] = useState("home");
  const [args, setArgs] = useState([]);

  const changePage =
    (newPage, newArgs = []) =>
    (e) => {
      e.preventDefault();
      if (newPage === page) return;

      setPage(newPage);
      setArgs(newArgs);
      window.location.hash = `#${newPage}/${newArgs.join("/")}`;
    };

  const menu = {
    home: "Home",
    gallery: "Gallery",
    about: "About",
  };

  const routes = {
    home: () => <HomePage changePage={changePage} />,
    gallery: () => <GalleryPage />,
    about: () => <AboutPage />,
    detail: () => <DetailPage />,
    error: () => <ErrorPage />,
  };

  useEffect(() => {
    const handleHashChange = () => {
      const { hash } = window.location;
      const [newPage, ...newArgs] = hash.substring(1).split("/");
      setPage(newPage || "home");
      setArgs(newArgs);
    };

    window.addEventListener("hashchange", handleHashChange);
    handleHashChange();

    return () => window.removeEventListener("hashchange", handleHashChange);
  }, []);

  return (
    <div className='container d-flex flex-column w-100 h-100 p-3 mx-auto'>
      <PageHeader page={page} onClickMenu={changePage} />
      <main className='p-4'>
        {routes[page]?.call(null, args) || routes["error"](args)}
      </main>
      <PageFooter />
    </div>
  );
}
