import {SET_INITIAL_DATA, SET_USER, TEST_CLIENT} from "../constants/action-types";

export const initialState = {
    user: false,
    app: {flashed_messages: []},
    clients: []
};

export function appReducer(state, action) {
    switch(action.type) {
        case SET_USER:
            return {user: action.payload};
        case SET_INITIAL_DATA:
            return {
                user: action.payload.user,
                app: action.payload.app,
                clients: action.payload.clients
            };
        default:
            throw new Error();
    }
}