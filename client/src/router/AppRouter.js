import React from 'react'

import {
    BrowserRouter as Router,
    Routes,
    Route
  } from "react-router-dom";

import Anasayfa from '../pages/Anasayfa';
import Category from '../pages/Category';




const AppRouter = () => {
  return (
    <div>
        <Router>
            <Routes>
                <Route path='/' element = {<Anasayfa/>} />
                <Route path='category/' element = {<Category/>} />
            </Routes>
        </Router>

    </div>
  )
}

export default AppRouter