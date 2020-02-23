module.exports = {
    entry: __dirname + '/webpack/js/index.jsx',
    output: {
        filename: 'App.js',
        path: __dirname + '/app/static/dist'
    },
    resolve: {
        extensions: ['.js', '.jsx']
    },
    module: {
        rules: [
            {
                test: /\.(js|jsx)$/,
                exclude: /node_modules/,
                use: {
                    loader: "babel-loader"
                }
            },
            {
                test: /\.html$/,
                use: {
                    loader: "file-loader?name=[name].[ext]"
                }
            }
        ]
    },
    devServer: {
        contentBase: __dirname + '/dist',
        compress: true,
        port: 8080
    }
};