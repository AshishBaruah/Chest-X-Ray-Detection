import './App.css';
import LandingPage from './LandingPage';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import SignInSide from './pages/SignIn/SignInSide';
import SignUp from './pages/SignUP/SignUp';
import * as React from 'react';
import AppAppBar from './components/AppAppBar';




function App() {
  return (
    
    <div className="App">
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<LandingPage/>}>
        </Route>
          <Route path="sign-in" element={<SignInSide/>} />
          <Route path="sign-up" element={<SignUp/>} />
      </Routes>
    </BrowserRouter>
    </div>
  );
}

export default App;
