const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
        transpileDependencies: true,
        devServer: {
            headers: {
                'Cache-Control': 'no-transform'
            },
            proxy: 'http://localhost:8000/'
        }
    }
)
