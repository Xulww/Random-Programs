import React, { useState, useEffect } from "react";
import { Text, View, Image, Dimensions } from "react-native";
import {
  Collapse,
  CollapseHeader,
  CollapseBody,
} from "accordion-collapse-react-native";
import { ListItem } from "native-base";
import MapView, { PROVIDER_GOOGLE } from "react-native-maps";
import { Marker } from "react-native-maps";
import * as firebase from "firebase";
import { globalStyles } from "../../../styles/globalStyles";

const { width, height } = Dimensions.get("window");
const ASPECT_RATIO = width / height;
const LATITUDE_DELTA = 0.0922;
const LONGITUDE_DELTA = LATITUDE_DELTA * ASPECT_RATIO;

const ProblemCard = (props) => {
  const [image, setImage] = useState("");

  useEffect(() => {
    let storageRef = firebase.storage().ref();
    let spaceRef = storageRef.child("images/" + props.photo);
    storageRef
      .child("images/" + props.photo)
      .getDownloadURL()
      .then((url) => {
        setImage(url);
      });
  }, []);

  return (
    <View style={globalStyles.card} key={props.id}>
      <Collapse style={globalStyles.collapse}>
        <CollapseHeader>
          <View style={{ flexDirection: "row", color: "red" }}>
            <Image style={globalStyles.photo} source={{ uri: image }} />
            {/* <Button title="delete" onPress={() => props.onDelete(props.id)}>
              Delete
            </Button> */}
          </View>
        </CollapseHeader>
        <CollapseBody>
          <ListItem>
            <MapView
              provider={PROVIDER_GOOGLE} // remove if not using Google Maps
              style={{ width: width - 20, height: 100, marginTop: 10 }}
              region={{
                latitude: Number(props.latitude),
                longitude: Number(props.longitude),
                latitudeDelta: Number(LATITUDE_DELTA),
                longitudeDelta: Number(LONGITUDE_DELTA),
              }}
              showsMyLocationButton={true}
              showsUserLocation={true}
            >
              <Marker
                coordinate={{
                  latitude: Number(props.latitude),
                  longitude: Number(props.longitude),
                  latitudeDelta: Number(LATITUDE_DELTA),
                  longitudeDelta: Number(LONGITUDE_DELTA),
                }}
                title={"Location"}
                description={"You are here!"}
              />
            </MapView>
          </ListItem>
          <ListItem style={globalStyles.listItem}>
            <Text>Name: {props.name}</Text>
          </ListItem>
          <ListItem style={globalStyles.listItem}>
            <Text>Surname: {props.surname}</Text>
          </ListItem>
        </CollapseBody>
      </Collapse>
    </View>
  );
};

export default ProblemCard;
