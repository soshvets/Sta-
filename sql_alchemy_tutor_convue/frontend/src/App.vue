<template>
  <div id="app" class="uk-container">
    <nav class="uk-navbar-container" uk-navbar>
      <div class="uk-navbar-center">
        <ul class="uk-navbar-nav">
          <li class="uk-active">
            <router-link to="/" class="uk-nav">Home</router-link>
          </li>
          <li>
            <router-link to="/departments">Departments</router-link>
          </li>
          <li>
            <router-link to="/workers">Workers</router-link>
          </li>
        </ul>
      </div>
    </nav>
    <router-view/>
  </div>
</template>

<style lang="scss">

@import "uikit/src/scss/variables-theme.scss";

@import "uikit/src/scss/mixins-theme.scss";

@import "uikit/src/scss/uikit-theme.scss";
nav{
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#app{
    font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}

</style>

