import React from "react";
import {Nav} from "./Nav";

export function ClientList(props) {
    return (
        <section className="content">
            <header>
                <h1>Oauth Clients</h1>
                {(props.user && props.app) ?
                    <a className={"action"} href="" >New</a> : ""}
            </header>
            {props.app.flashed_messages.length > 0 ?
                props.app.flashed_messages.map((message) =>
                    <div className={"flash"}>{message}</div>
                ) : ""}
            {props.clients.length > 0 ?
                props.clients.map((client, i) =>
                    [
                        <article key={"client-" + client.client_id} className={"post"}>
                            <header>
                                <div>
                                    <h1>{client.name}</h1>
                                    <p>{client.description}</p>
                                    <ul>
                                        <li>
                                            <span>Client ID: {client.client_id}</span>
                                        </li>
                                        <li>
                                            <span>Client Secret: {client.client_secret}</span>
                                        </li>
                                    </ul>
                                </div>
                                <a className={"action"} href="#">Edit</a>
                                <a className={"action"} href="#"
                                   onClick={() => props.testClient(client)}>Test</a>
                            </header>
                        </article>,
                        i === props.clients.length - 1 ? "" : <hr key={"hr-" + client.client_id} />
                    ]
                )
                : ""}
        </section>

    )
}