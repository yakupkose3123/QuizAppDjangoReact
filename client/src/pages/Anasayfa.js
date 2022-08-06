import React, {useEffect, useState, useNavi}from 'react'
import { useNavigate } from 'react-router-dom';



const Anasayfa = () => {
    const [category, setCategory] = useState([]);
    const navigate = useNavigate()

    const getCategory = () => {
        fetch("http://127.0.0.1:8000/quiz/")
        .then((response) => response.json())
        .then((data) => {
          console.log(data);
          setCategory(data);          
        })
        .catch((err) => console.log(err));
    };


    useEffect(() => {            
        getCategory();
        
    }, []);



  return (
    <div className='m-auto w-75'>
        <h1>SELECT CATEGORY FOR QUIZ</h1>
        {
            category.map((cat) =>
            <button type="submit" className='btn btn-danger m-5'> {cat.name}</button> 
            )
        }

    </div>
  )
}

export default Anasayfa