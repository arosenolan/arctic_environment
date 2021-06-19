const path = require('path');

module.exports = {
    entry: {
        aframedemo: './tools_for_curiousity_app/t4c/js/aframedemo.js',
    },
    output: {
        path: path.resolve(__dirname, './tools_for_curiousity_app/t4c/static/t4c/dist/'),
        publicPath: '/static/t4c/dist',
        filename: '[name].bundle.js'
    }
}