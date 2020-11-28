import React, { useEffect, useState } from "react";
import {
  Text,
  View,
  Image,
  TextInput,
  Button,
  Alert,
  Dimensions,
  TouchableOpacity,
} from "react-native";
import MapView, { PROVIDER_GOOGLE } from "react-native-maps";
import { Marker } from "react-native-maps";
import * as ImagePicker from "expo-image-picker";
import * as SQLite from "expo-sqlite";
import * as firebase from "firebase";
import { globalStyles } from "../../styles/globalStyles";

const { width, height } = Dimensions.get("window");
const ASPECT_RATIO = width / height;
const LATITUDE_DELTA = 0.0922;
const LONGITUDE_DELTA = LATITUDE_DELTA * ASPECT_RATIO;

const db = SQLite.openDatabase("ConscientiousDrivers.db");

const Submit = ({ navigation }) => {
  const [fname, setFname] = useState("");
  const [lname, setLname] = useState("");
  const [latitude, setLatitude] = useState(0);
  const [latitudeDelta, setLatitudeDelta] = useState(0);
  const [longitude, setLongitude] = useState(0);
  const [longitudeDelta, setLongitudeDelta] = useState(0);
  const [photo, setPhoto] = useState("");
  const [photoUri, setPhotoUri] = useState("");

  useEffect(() => {
    navigator.geolocation.getCurrentPosition(
      (position) => {
        let lat = parseFloat(position.coords.latitude);
        let long = parseFloat(position.coords.longitude);
        setLatitude(lat);
        setLongitude(long);
        setLatitudeDelta(LATITUDE_DELTA);
        setLongitudeDelta(LONGITUDE_DELTA);
      },
      (error) => {
        Alert.alert(String(error.message));
      },
      { enableHighAccuracy: false, timeout: 20000 }
    );
  }, []);

  const insertData = (fname, lname, latitude, longitude, photo) => {
    let query =
      "INSERT INTO PROBLEMS (ID, FNAME, LNAME, LATITUDE, LONGITUDE, PHOTO) VALUES (null, ?, ?, ?, ?, ?)";
    let params = [
      fname,
      lname,
      String(latitude),
      String(longitude),
      String(photo),
    ];
    db.transaction((tx) => {
      tx.executeSql(
        query,
        params,
        (tx, results) => {
          Alert.alert("The problem has been added!");
        },
        (tx, err) => {
          Alert.alert(String(err));
          return;
        }
      );
    });

    // this sends the problem the user just added to the main component
    let randomId = Math.random().toString(36).substring(7);
    navigation.navigate("Home", {
      FNAME: fname,
      LNAME: lname,
      ID: randomId,
      LATITUDE: String(latitude),
      LONGITUDE: String(lname),
      PHOTO: String(photo),
    });
  };

  const handleSave = () => {
    if (
      (fname !== "" && lname !== "" && latitude !== "" && longitude !== "",
      photo !== "")
    ) {
      insertData(fname, lname, String(latitude), String(longitude), photo);
    } else {
      Alert.alert("Warning", "has not been saved");
    }
  };

  const uploadImage = async (uri, name) => {
    const response = await fetch(uri);
    const blob = await response.blob();

    let ref = firebase
      .storage()
      .ref()
      .child("images/" + name);

    return ref.put(blob);
  };

  const openImage = async () => {
    // if you want to access the camera you will have to use the function launchCameraAsync()
    // which will return you a photo once the user has taken one
    // https://docs.expo.io/versions/latest/sdk/imagepicker/#imagepickerlaunchcameraasyncoptions
    let permission = await ImagePicker.requestCameraPermissionsAsync();

    if (permission.granted === false) {
      return;
    }

    let picker = await ImagePicker.launchImageLibraryAsync();
    let randomName = Math.random().toString(36).substring(7);
    setPhoto(randomName);
    setPhotoUri(picker.uri);
    uploadImage(picker.uri, randomName);
  };

  return (
    <>
      <View style={globalStyles.container}>
        <Text>You are here</Text>
        <MapView
          provider={PROVIDER_GOOGLE} // remove if not using Google Maps
          style={{ width: width - 40, height: 150 }}
          region={{
            latitude: Number(latitude),
            longitude: Number(longitude),
            latitudeDelta: Number(latitudeDelta),
            longitudeDelta: Number(longitudeDelta),
          }}
          showsMyLocationButton={true}
          showsUserLocation={true}
        >
          <Marker
            coordinate={{
              latitude: Number(latitude),
              longitude: Number(longitude),
              latitudeDelta: Number(latitudeDelta),
              longitudeDelta: Number(longitudeDelta),
            }}
            title={"Location"}
            description={"You are here!"}
          />
        </MapView>
        {photo ? (
          <Image style={globalStyles.photo} source={{ uri: photoUri }} />
        ) : null}
        <TextInput
          style={globalStyles.textInput}
          placeholder="First Name"
          value={fname}
          onChangeText={(val) => setFname(val)}
        />
        <TextInput
          style={globalStyles.textInput}
          placeholder="Last Name"
          value={lname}
          onChangeText={(val) => setLname(val)}
        />
        <TextInput
          style={globalStyles.hidden}
          placeholder="Latitude"
          value={String(latitude)}
          onChangeText={(val) => setLatitude(Number(val))}
        />
        <TextInput
          style={globalStyles.hidden}
          placeholder="Longitude"
          value={String(longitude)}
          onChangeText={(val) => setLongitude(Number(val))}
        />
        <TextInput
          style={globalStyles.hidden}
          placeholder="Photo"
          value={String(photo)}
          onChangeText={(val) => setPhoto(String(val))}
        />
        <TouchableOpacity style={globalStyles.uploadButton} onPress={openImage}>
          <Text>Upload Photo</Text>
        </TouchableOpacity>
        <Button title="Submit" onPress={handleSave} />
      </View>
    </>
  );
};

export default Submit;
