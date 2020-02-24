import React, { useReducer, useEffect } from 'react';
import axios from 'axios';
import {setInitialData, setUser, testClient} from "../actions";
import {appReducer, initialState} from "../reducers";
import {Nav} from "../presentation/Nav";
import {ClientList} from "../presentation/ClientList";
import {HashRouter as Router, Route, Switch} from "react-router-dom";
import {ApiTest} from "../presentation/ApiTest";


export default function App() {
  const [state, dispatch] = useReducer(appReducer, initialState);

  useEffect(() => {
      axios('/index/get_initial_data')
          .then((result) => {
              dispatch(setInitialData(result.data))
          });
  }, []);

  return (
      <div>
          <Nav user={state.user} app={state.app} />
          <Router>
            <Switch>
                <Route exact path="/">
                  <ClientList
                      testClient={(client) => dispatch(testClient(client))}
                      user={state.user}
                      app={state.app}
                      clients={state.clients} />
                </Route>
                <Route path="*">
                    <ApiTest />
                </Route>
            </Switch>
        </Router>
      </div>
  );
}


