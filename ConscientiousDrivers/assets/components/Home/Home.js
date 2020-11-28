import React, { useState, useEffect } from "react";
import { Button, Alert } from "react-native";
import ProblemCard from "./ProblemCard/ProblemCard";
import * as SQLite from "expo-sqlite";
import * as firebase from "firebase";
import ApiKeys from "../../ApiKeys";
import { ScrollView } from "react-native-gesture-handler";

const db = SQLite.openDatabase("ConscientiousDrivers.db");

const Home = ({ navigation }) => {
  const [problems, setProblems] = useState([]);

  const fetchData = () => {
    let query = "SELECT * FROM PROBLEMS";
    let params = [];
    db.transaction((tx) => {
      tx.executeSql(
        query,
        params,
        (tx, results) => {
          if (results.rows._array.length > 0) {
            setProblems(results.rows._array);
          }
        },
        (tx, err) => {
          Alert.alert(String(err));
        }
      );
    });
  };

  useEffect(() => {
    if (!firebase.apps.length) {
      firebase.initializeApp(ApiKeys.FirebaseConfig);
    }

    db.transaction((tx) => {
      tx.executeSql(
        "CREATE TABLE IF NOT EXISTS PROBLEMS (ID INTEGER PRIMARY KEY AUTOINCREMENT, FNAME CHAR(255) NOT NULL, LNAME CHAR(255) NOT NULL, LATITUDE CHAR(100) NOT NULL, LONGITUDE CHAR(100) NOT NULL, PHOTO CHAR(255) NOT NULL);"
      );
    });

    fetchData();
  }, []);

  // this hook updates the array when a new problem is added
  // useEffect(() => {
  //   const objToUpdateArr = {
  //     ID: navigation.getParam("ID"),
  //     FNAME: navigation.getParam("FNAME"),
  //     LNAME: navigation.getParam("LNAME"),
  //     LATITUDE: navigation.getParam("LATITUDE"),
  //     LONGITUDE: navigation.getParam("LONGITUDE"),
  //     PHOTO: navigation.getParam("PHOTO"),
  //   };

  //   setProblems([...problems, objToUpdateArr]);
  // }, [navigation.getParam("FNAME")]);

  const pressHandler = () => {
    // navigation.push('Submit')
    navigation.navigate("Submit");
  };

  // const deleteRow = (id) => {
  //   let query = "DELETE FROM PROBLEMS WHERE ID = ?";
  //   let params = [id];
  //   db.transaction((tx) => {
  //     tx.executeSql(
  //       query,
  //       params,
  //       (tx, results) => {
  //         console.log("success");
  //       },
  //       (tx, error) => {
  //         console.log(error);
  //       }
  //     );
  //   });
  // };

  return (
    <>
      <ScrollView>
        <Button
          style={{ alignSelf: "stretch" }}
          title="Submit"
          onPress={pressHandler}
        />
        {problems.map((problem) => {
          return (
            <ProblemCard
              key={problem.ID}
              id={problem.ID}
              name={problem.FNAME}
              surname={problem.LNAME}
              latitude={problem.LATITUDE}
              longitude={problem.LONGITUDE}
              photo={problem.PHOTO}
              // onDelete={deleteRow}
            />
          );
        })}
      </ScrollView>
    </>
  );
};

export default Home;
