// const path = require('path')

module.exports = {
  transpileDependencies: true,

  devServer: {
    proxy:
      'http://127.0.0.1:8000'
      // {
      //   "^/api/v1": {
      //     target: "http://127.0.0.1:8000/",
      //     changeOrigin: true,
      //     compress: false,
      //     headers: {
      //       "Cashe-Control": "no-transform",
      //     },
      //   },
      //   // '^/api/v1/push/stream': {
      //   //   target: 'http://localhost:8000',
      //   //   changeOrigin: true,
      //   //   compress: false,
      //   //   headers: {
      //   //     'Cache-Control': 'no-transform'
      //   //   },
      //   // }
      // },
  }
};
