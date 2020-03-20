import React from "react";
import App, { Container } from "next/app";
import withRedux from "next-redux-wrapper";
import makeStore from "store/index"
import {Provider} from "react-redux";


class MyApp extends App {
  render() {
    const { Component, pageProps, store } = this.props;
    return (
      <Provider store={store}>
          <Component {...pageProps} />
      </Provider>
    );
  }
}

export default withRedux(makeStore)(MyApp);
