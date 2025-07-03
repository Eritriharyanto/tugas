import { useContext } from 'react'
import SessionContext from '../SessionContext'
import Home from '../pages/Home'
import Profile from '../pages/Profile'
import Error from '../pages/Error'
import Login from '../pages/Login'

export default function AppBody() {
  const [session] = useContext(SessionContext)
  const routes = {
    'home': <Home />,
    'profile': <Profile />,
    'login': <Login />,
  }

  return routes[session.page] ?? <Error />;
}
