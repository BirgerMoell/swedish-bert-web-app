import React, { useState, fragment } from 'react';
import kb from './kb.png';
import './App.css';

function App() {

  const [text, setText] = useState("")
  const [ner, setNer] = useState([])

async function namedEntityRecognition(text) {
  let data = {
    text: text
  }

  let response = await fetch("http://localhost:8020/ner", 
    {
    method: "POST",
    contentType: "application/json",
    body: JSON.stringify(data)
  })

  let responseJson = await response.json()

  console.log("the response json", responseJson)

  if (responseJson && responseJson.text) {
    setNer(responseJson.text)
  }

  return responseJson
}

  return (
    <div className="App">
      <header className="App-header">

        <img src={kb} height="100px" width="100px"/>
       <p>Kungliga Biblioteket BERT Model</p>

       <h5>Named Entity Recognition</h5>
       <p className="small">Named Entity Recognition är att plocka ut kategorier från
         ostrukturead text. Vanliga kategorier är namn, organisation och plats.
       </p>
       <textarea onChange={(e) => setText(e.target.value)}></textarea>
       <button onClick={() => namedEntityRecognition(text)}>Named Entity Recognition</button>

        {ner && ner.map (item =>
        <fragment>
           <span className="small word">| {item.word} </span>
          <span className="small entity">{item.entity} </span>
          <span className="small index">{item.index} |</span>
         
          </fragment> 
          )}

  
      </header>
    </div>
  );
}

export default App;
