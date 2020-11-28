import { StyleSheet } from "react-native";

export const globalStyles = StyleSheet.create({
  photo: {
    width: 200,
    height: 200,
    resizeMode: "contain",
  },
  card: {
    textAlign: "center",
    borderBottomWidth: 1,
    borderStyle: "solid",
    borderColor: "grey",
    alignItems: "center",
  },
  container: {
    flex: 1,
    backgroundColor: "#fff",
    alignItems: "center",
    justifyContent: "center",
  },
  welcomeText: {
    marginTop: 10,
    fontSize: 25,
  },
  hidden: {
    opacity: 0,
    height: 0,
  },
  uploadButton: {
    borderRadius: 10,
    borderWidth: 1,
    borderColor: "#2196F3",
    margin: 10,
    justifyContent: "center",
    alignItems: "center",
    padding: 5,
    color: "white",
  },
  textInput: {
    borderWidth: 1,
    borderRadius: 10,
    height: 50,
    width: 300,
    margin: 10,
    padding: 5,
  },
  listItem: {
    marginBottom: 3,
    marginTop: 3,
  },
  collapse: {
    marginBottom: 30,
    marginTop: 10,
  },
});
