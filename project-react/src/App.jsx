import { SessionProvider } from "./SessionContext";
import AppHeader from "./components/AppHeader";
import AppBody from "./components/AppBody";
import AppFooter from "./components/AppFooter";

export default function App() {
  return (
    <SessionProvider>
      <AppHeader />
      <AppBody />
      <AppFooter />
    </SessionProvider>
  );
}
