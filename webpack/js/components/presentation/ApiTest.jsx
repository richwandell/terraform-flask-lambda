import React from "react";

export function ApiTest(props) {
    const paramsArray = Array.from(window.location.hash.matchAll(/(\w+)=(\w+)/ig));

    return (
        <div>
            <ul>
                {paramsArray.map((item) => {
                    return <li key={item[1]}>{item[1]}: {item[2]}</li>
                })}
            </ul>
        </div>
    )
}