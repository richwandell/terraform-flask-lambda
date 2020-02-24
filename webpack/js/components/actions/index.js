import {SET_INITIAL_DATA, SET_USER, TEST_CLIENT} from "../constants/action-types";

export function setUser(data) {
    return {type: SET_USER, payload: data};
}

export function setInitialData(data) {
    return {type: SET_INITIAL_DATA, payload: data};
}

export function testClient(client) {
    let url = [
        `/oauth/authorize?`,
        `client_id=${client.client_id}`,
        `&client_secret=${client.client_secret}`,
        `&response_type=token`,
        `&scope=local`,
        `&redirect_uri=http://localhost:5000`
    ].join("");
    window.location.href = url;
}