import React from "react";

export function Nav(props) {
    return (
        <nav>
          <h1>API</h1>
          <ul>
              {(props.user && props.app) ? [
                  <li key={"username"}><span>{props.user.username}</span></li>,
                  <li key={"url_for_auth_logout"}><a href={props.app.url_for_auth_logout} >Log Out</a></li>
              ] : [
                  <li key={"url_for_auth_register"}><a href={props.app.url_for_auth_register}>Register</a></li>,
                  <li key={"url_for_auth_login"}><a href={props.app.url_for_auth_login}>Log In</a></li>
              ]}
          </ul>
        </nav>
    )
}