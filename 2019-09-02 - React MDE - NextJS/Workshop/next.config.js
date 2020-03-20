const path = require('path');
const withSass = require('@zeit/next-sass')

module.exports = withSass({
  cssModules: true,
  webpack: (config) => {
    config.resolve.modules.push(path.resolve('./'));

    config.module.rules.push({
      enforce: 'pre',
      test: /.scss$/,
      loader: 'sass-resources-loader',
      options: {
        resources: ['./styles/globals.scss'],
      },
    });

    config.module.rules.push(
      {
        test: /\.svg$/,
        exclude: /node_modules/,
        loader: 'svg-react-loader',
      },
    );

    return config;
  },
});
