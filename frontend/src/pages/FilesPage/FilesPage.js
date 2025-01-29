import React from "react";
import { useEffect, useState } from "react";
import useAuth from "../../hooks/useAuth";

import axios from "axios";

const FilesPage = () => {
  // The "user" value from this Hook contains the decoded logged in user information (username, first name, id)
  // The "token" value is the JWT token that you will send in the header of any request requiring authentication
  //TODO: Add an AddCars Page to add a car for a logged in user's garage
  const [user, token] = useAuth();
  const [files, setFiles] = useState([]);
  const BaseURL = "http://127.0.0.1:8000";
  useEffect(() => {
    const fetchFiles = async () => {
      try {
        let response = await axios.get("http://127.0.0.1:8000/api/files/", {
          headers: {
            Authorization: "Bearer " + token,
          },
        });
        setFiles(response.data);
      } catch (error) {
        console.log(error.response.data);
      }
    };
    fetchFiles();
  }, [token]);
  return (
    <div className="container">
      <h1>Home Page for {user.username}!</h1>
      {files &&
        files.map((file) => (
          <div key={file.id}>
            <h2>{file.title}</h2>
            <p>{file.description}</p>
            <img width="100" height="100" src={BaseURL + file.file} alt={file.title} />
          </div>
        ))}
    </div>
  );
};

export default FilesPage;
