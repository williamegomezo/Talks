// next.config.js
const withSass = require('@zeit/next-sass');


module.exports = withSass({
  webpack: (config) => {
    config.module.rules.push({
      enforce: 'pre',
      test: /.scss$/,
      loader: 'sass-resources-loader',
      options: {
        resources: ['./styles/globals.scss'],
      },
    });
    return config;
  },
  cssModules: true,
  cssLoaderOptions: {
    importLoaders: 1,
    localIdentName: '[local]',
  },
});