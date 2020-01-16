const path = require('path');
module.exports = {
    mode: 'production',
    entry: {
        "main1": path.resolve(__dirname, 'src/index.ts'),
        "main2": path.resolve(__dirname, 'src/index2.ts')
    },
    output: {
        path: path.resolve(__dirname, 'dist'),
        filename: '[name].js',
        libraryTarget: "umd"
    },
    module: {
        rules: [
            {
                test: /\.ts/,
                exclude: /(node_modules)/,
                use: {
                    loader: 'ts-loader'
                }
            },
            {
                test: /\.css/,
                use: [
                    "style-loader",
                    "css-loader"
                ]
            }
        ]
    },
    resolve:{
        extensions: ['.ts', '.js']
    }
}