import { createStackNavigator } from "react-navigation-stack";
import { createAppContainer } from "react-navigation";
import Home from "../Home/Home";
import Submit from "../Submit/Submit";

const screens = {
  Home: {
    screen: Home,
    navigationOptions: {
      title: "Dashboard",
    },
  },
  Submit: {
    screen: Submit,
    navigationOptions: {
      title: "Submit",
    },
  },
};

const HomeStack = createStackNavigator(screens, {
  defaultNavigationOptions: {
    headerStyle: { backgroundColor: "#fc6404" },
    headerTitleStyle: { color: "#eee" },
    headerTintColor: "#eee",
  },
});

export default createAppContainer(HomeStack);
