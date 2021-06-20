const path = require('path');

module.exports = {
    entry: {
        aframedemo: './tools_for_curiousity_app/t4c/js/aframedemo.js',
    },
    devtool: 'source-map', // TODO: this works nicely in development for Safari + Chrome, but is slow. We should also change when building for production.
    output: {
        path: path.resolve(__dirname, './tools_for_curiousity_app/t4c/static/t4c/dist/'),
        publicPath: '/static/t4c/dist',
        filename: '[name].bundle.js'
    }
}