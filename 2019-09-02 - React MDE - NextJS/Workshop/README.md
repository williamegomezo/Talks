# Contents:

1. [Initial setup](#initial_setup)
2. [CSS and SCSS](#css)
3. [Basic Routing](#routing)
4. [Static files, handle svgs](#static)
5. [Dynamic Routing](#dynamic)
6. [Redux](#redux)
7. [API for external users](#api)

# Workshop

<span id="#initial_setup" >
1.  Initial Setup: <a name="initial_setup"></a>

  To create a next project, we only need to create a folder and init a npm project:

        mkdir Workshop
        cd Workshop
        npm init

  Install NextJS packages and dependencies:

        npm install --save next react react-dom

  Add the following scripts in your package.json:

        "scripts": {
            "dev": "next",
            "build": "next build",
            "start": "next start"
        }

  Let's test if everything is working, create a folder called `pages`:

        mkdir pages

  Create a javascript file (the name of the file will be taken by NextJS as the route where the page will be set)
  and create a react component:

  `hello.js`

        function Hello() {
            return <p>Hello NextJS!</p>;
        }

        export default Hello;

  Let's run the dev server:

        npm run dev

  In the address `http://localhost:3000/hello` we should watch our first page in NextJS.

  Let's create a component and import it in our page.

  Create a folder called `components` and inside another one called `cta`:

        mkdir components

        mkdir cta

  Create a file called `cta.js`:

        class Cta extends React.Component {
          render() {
            return <button>Click me</button>
          }
        }

  Let's import it in our `hello` page.

        import Cta from '../components/cta/cta'

        function Hello() {
            return <Cta />;
        }

        export default Hello;

  So far we are good, but let's improve our code:

### 1. Config File
  If our project scales, there will be a moment when the relative imports will be like the following
  `../../../../package.js` and will be difficult to track or modify something, that's why we will start
  configuring the absolute import:

  In NextJS there is a config file that we need to create `next.config.js` which allows us to have a custom
  configuration. In this file we can change how long will last the caching, how will be called our `dist` folder,
  set additional webpack configuration and so on. Let's customize our webpack in order to have absolute import:

  First create `next.config.js` in the root directory of our project:

    `next.config.js`
    module.exports = {}

  When we are working with webpack without NextJS, that is, we install webpack ourselves and create a `webpack.config.js`, to have a absolute import you must set the following:

  `webpack.config.js`

        resolve: {
          modules: [
            path.resolve('./')
          ]
        }

  In NextJS, the json exported in `next.config.js` can have a field called webpack:

  `next.config.js`

        module.exports = {
          webpack: (config, options) => {
            // Here modify anything you need about the config.
            return config
          }
        }

  So, what we are going to do is to set the config in the following way:

  `next.config.js`

        const path = require('path')

        module.exports = {
          webpack: (config, options) => {
            config.resolve.modules.push(path.resolve('./'))
            return config
          }
        }

  Setting that, we can now modify the import we had on `pages/hello.js`

        import Cta from 'components/cta/cta'

  Perfect, now you are much closer to be a pro coder.

  ### 2. Linters!
  How did you bear a code without linters? Let's install eslint to help us to set a standard linter configuration...

  Run in the terminal:

        npm install -g eslint

        eslint --init

  Select:

    1. ❯ To check syntax, find problems, and enforce code style
    2. ❯ JavaScript modules (import/export)
    3. ❯ Vue.js ... kidding ❯ React
    4. Does your project use TypeScript? ❯ Obviously not!
    5. ❯ Browser
    6. ❯ Use a popular style guide
    7. ❯ Airbnb (https://github.com/airbnb/javascript)
    8. ❯ JavaScript
    9. ❯ (missing dependencies) ... install them with npm? ❯ Y

  We will end with a `.eslintrc.js` file in our root path.

  If we have in vscode the eslint extension you will notice that the IDE will be warning us with every lint error.

  There are some additions we should include in our `.eslintrc.js` config, because we dont want to deal with them:

  - 'React' must be in scope when using JSXeslint(react/react-in-jsx-scope)
  - JSX not allowed in files with extension '.js'eslint(react/jsx-filename-extension)

  So, let's add to the file the following rules:

        "rules": {
          "react/react-in-jsx-scope": "off",
          "react/jsx-filename-extension": [1, { "extensions": [".js", ".jsx"] }],
          "react/prop-types": [0]
        }

  But, we will still have to set some settings to avoid warnings about absolute import and other react features, first install `babel-eslint`:

        npm install eslint@4.x babel-eslint@8 --save-dev

  Then add this to the `.eslintrc.js` file:

        "settings": {
          "import/resolver": {
            "node": {
              "paths": ["./"]
            }
          },
          "react": {
            "pragma": "React",
            "version": "16.9.0"
          }
        },
        "parser": "babel-eslint",

  Almost ready, add in the globals the React field, like this:

        "globals": {
          "Atomics": 'readonly',
          "SharedArrayBuffer": 'readonly',
          "React": 'writable',
        }

  To avoid that eslint warns us about having React without importing, actually NextJS is importing it in background.

  If we run:

        eslint .

  We will see only warnings of our lack of seniority.


<span id="#css" >
2.  CSS and SCSS configuration: <a name="css"></a>

  Well, first, NextJS in its documentation shows a Built-in CSS support, which uses `styled-jsx` to isolated scoped CSS. This is the example provided by them:

        function HelloWorld() {
          return (
            <div>
              Hello world
              <p>scoped!</p>
              <style jsx>{`
                p {
                  color: blue;
                }
                div {
                  background: red;
                }
                @media (max-width: 600px) {
                  div {
                    background: blue;
                  }
                }
              `}</style>
              <style global jsx>{`
                body {
                  background: black;
                }
              `}</style>
            </div>
          )
        }

        export default HelloWorld;

  In this tutorial we are not going to use this, because I don't like it :P

  We will be using scss files, and for that we need a dependency: `next-sass`

  We can find the package in the following link:
  https://github.com/zeit/next-plugins/tree/master/packages/next-sass

  Its installation is really easy:

        npm install --save @zeit/next-sass node-sass

  To use it we only need to wrap the exported json of `next.config.js`:

  `next.config.js`

        const withSass = require('@zeit/next-sass')

        module.exports = withSass({
          /* config options here */
        })

  That is enough to style our cta:

  Create in `components/cta/` a file `cta.scss`:

  `components/cta/cta.scss`

        .superCta {
          background-color: white;
          font-size: 20px;
          border: 1px solid;
        }

  `components/cta/cta.js`

        import './cta.scss';

        class Cta extends React.Component {
          render() {
            return <button className='superCta'>Click me</button>;
          }
        }

        export default Cta;

  Cool, now we can use scss. What if we use the cool CSS Modules?

  Add field cssModules in `next.config.js`

        module.exports = withSass({
          ...,
          cssModules: true
        })

  And change `components/cta/cta.js` for:

        import css from './cta.scss';

        class Cta extends React.Component {
          render() {
            return <button className={css.superCta}>Click me</button>;
          }
        }

        export default Cta;

  `css` is a map, with the name of the class is scss and the hash name generated for CSS modules. Example:

        {
          superCta: "oz3A60u9ZTGJI-7A1n1go"
        }

  In the browser we have:

        <button class="oz3A60u9ZTGJI-7A1n1go">Click me</button>

  There is a problem we haven't tackle, what if we want global styles, like resets, colors, media queries?

  We need to install a new dependency `sass-resources-loader`

        npm install sass-resources-loader

  And again, let's add more rules to our `next.config.js`:

        webpack: (config) => {
            ...;

            config.module.rules.push({
              enforce: 'pre',
              test: /.scss$/,
              loader: 'sass-resources-loader',
              options: {
                resources: ['./styles/globals.scss'],
              },
            });

            return config;
        }

  Basically we are adding a rule, where it will look in a folder called `styles` (that we are going to create in the
  root folder) and it will look for a file called `globals.scss` (set the name you want, it could be `main.scss`)

  There in `styles/globals.scss` you can import any file you want to have as a global resource in every page:

  For example, import a reset.scss:

        @import './reset.scss';
  
  Of course `reset.scss` have to exist, and it could be:

```scss
        * {
          margin: 0;
          padding: 0;
        }
```

<span id="#routing" >
3.  Routing:

  To make this more entertaining, let's create an app with purpose.

  Let's create the Tour of Heroes of our enemy!

  https://moynokylxexp.angular.stackblitz.io/dashboard

  So, we have to create three pages:

  /dashboard
  /heroes
  /detail/:id

  We will let the third one for the step of dynamic routing

  Create two js files in the folder `pages`: `dashboard.js` and `heroes.js`

  `pages/dashboard.js`

        function Dashboard() {
          return <div>
            // Navigation Bar
            <h1>Tour of Heroes</h1>
            // Hero search
            // Top of Heroes (List component)
          </div>;
        }

        export default Dashboard;

  `pages/heroes.js`

        function Heroes() {
          return <div>
            // Navigation Bar
            <h1>Heroes</h1>
            // Hero add
            // List of heroes (List component)
          </div>;
        }

        export default Heroes;

  Check the routing visiting:

  http://localhost:3000/dashboard

  http://localhost:3000/heroes

  Well, now, how can we go from one page to another?

  Let's modify our Cta component to have the Link component of NextJS:

  `components/cta/cta.js`

    import Link from "next/link";
    import css from "./cta.scss";

        function Cta(props) {
          const { href, callback, children } = props;

          return href ? (
            <Link href={href}>
              <a className={css.superCta}>{children}</a>
            </Link>
          ) : (
            <button className={css.superCta} onClick={callback}>
              {children}
            </button>
          );
        }

        export default Cta;

  We add Link from "next/link" which allows as to having a kind of SPA routing in a SSR app.

  Let's modify our pages:

  `pages/dashboard.js`

        import Cta from 'components/cta/cta';

        function Dashboard() {
          return <div>
            <Cta href="/heroes">Go to heroes list</Cta>
            <h1>Tour of Heroes</h1>
            // Hero search
            // List of Heroes
          </div>;
        }

        export default Dashboard;

  `pages/heroes.js`

        import Cta from 'components/cta/cta';

        function Heroes() {
          return (
            <div>
              <Cta href="/dashboard">Go to dashboard</Cta>
              <h1>Heroes</h1>
              // Hero add // List of heroes (List component)
            </div>
          );
        }

        export default Heroes;

  Our Cta looks ugly, I will add some styles to it.

        .superCta {
          display: inline-block;
          background-color: white;
          color: black;
          font-family: 'Roboto';
          font-weight: 500;
          font-size: 20px;
          border: 1px solid;
          text-decoration: none;
          padding: 10px;
          margin: 10px;
        }

<span id="#static" >
4.  Static files:

  Handling static files is easy, you must create only one folder -> `static`, there you put any assets you want.

  Let's download an image:
    https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/React.svg/1200px-React.svg.png

  And put in `./static/images/react.png`

  Remember our `hello` page?

  `pages/hello.js`

        function Hello() {
          return <div>
            <h1>Hello React MDE</h1>
            <img src="/static/images/react.png" alt="React MDE" />
          </div>;
        }

        export default Hello;

  There is also another way to handle static files and is importing then, and using libraries to load them:

  SVGs:

  Dependencies everywhere: Let's install `svg-react-loader`

  Again we have to modify our webpack config, adding the following rule:

        config.module.rules.push(
          {
            test: /\.svg$/,
            exclude: /node_modules/,
            loader: 'svg-react-loader',
          },
        );

  Go to material icons: https://material.io/resources/icons/?style=baseline

  And search for `search`, save the icon <img src='./static/icons/search.svg'> in the folder `/static/icons/`.

  Now, let's load it. But first, let's create another component, a search bar:

  `components/searchBar.js`

        import css from "./searchBar.scss";

        function SearchBar(props) {
          const { placeholder } = props;

          return (<div className={css.searchBar}>
            // Here there should be a search icon
            <input placeholder={placeholder} />
          </div>);
        }

        export default SearchBar;

  Now let's add the svg:

        import SearchIcon from 'static/icons/search.svg';

  And ...

        function SearchBar(props) {
          const { placeholder } = props;

          return (<div className={css.searchBar}>
            <SearchIcon />
            <input placeholder={placeholder} />
          </div>);
        }

        export default SearchBar;

  It would be better to wrap SearchIcon in a component maybe called `SvgIcon` and load dynamically the svg based on a prop.
  That will be done creating:


  `components/svgIcon.js`

        function SvgIcon(props) {
          const { iconName } = props;
          const Icon = require(`static/icons/${iconName}.svg`);
          return <Icon />;
        }

        export default SvgIcon;

  `components/searchBar/searchBar.js`

        import SvgIcon from "components/svgIcon/svgIcon";
        import css from "./searchBar.scss";

        function SearchBar(props) {
          const { placeholder } = props;

          return (
            <div className={css.searchBar}>
              <div className={css.searchIcon}>
                <SvgIcon iconName="search" />
              </div>
              <input className={css.searchInput} placeholder={placeholder} />
            </div>
          );
        }

        export default SearchBar;

  I will add some styles to the searchBar:

  `components/searchBar/searchBar.scss`

        .searchBar {
          position: relative;
          font-family: 'Roboto';
          width: 200px;
          height: 40px;
        }

        .searchIcon {
          position: absolute;
          top: 50%;
          left: 5px;
          z-index: 1;
          transform: translateY(-50%);
        }

        .searchInput {
          position: absolute;
          top: 0;
          left: 0;
          width: 200px;
          height: 40px;
          font-size: 20px;
          padding-left: 30px;
        }

  And dashboard should be:

    `pages/dashboad.js`

        import Cta from 'components/cta/cta';
        import SearchBar from 'components/searchBar/searchBar';

        function Dashboard() {
          return <div>
            <Cta href="/heroes">Go to heroes list</Cta>
            <h1>Tour of Heroes</h1>
            <SearchBar placeholder="Search a hero"/>
            // List of Heroes
          </div>;
        }

        export default Dashboard;

  Well, in order to have heroes, for now we will mock them:

    `static/mocks/heroes.json`

        [
          'Wolverine',
          'Spider-Man',
          'Thor',
          'Iron Man',
          'Hulk',
          'Captain America',
          'Daredevil',
          'Punisher',
          'William Gomez',
        ]

  Now, we know that the heroes will be on the route `localhost:3000/static/mocks/heroes.json`, obviously we can import them,
  but there is more fun if we fetch them, I will use the love of my live which is called axios, let's install it:

        npm install axios

  Now, let's use a functionality of NextJS that allow us to get an initial status of the page: `getInitialProps`

  Our dashboard will look like:

  `pages/dashboad.js`

        import Cta from "components/cta/cta";
        import SearchBar from "components/searchBar/searchBar";
        import axios from "axios";

        function Dashboard(props) {
          const { heroes } = props;

          return (
            <div>
              <Cta href="/heroes">Go to heroes list</Cta>
              <h1>Tour of Heroes</h1>
              <SearchBar placeholder="Search a hero" />
              { heroes.length > 1 && (
                <ol>
                  {heroes.map(hero => <li>{hero}</li>)}
                </ol>
              )}
            </div>
          );
        }

        Dashboard.getInitialProps = async () => {
          const res = await axios.get('http://localhost:3000/static/mocks/heroes.json');
          const heroes = await res.data;
          return { heroes };
        };

        export default Dashboard;

  For now, our search bar does not work, let's wait to redux part to make it work.

  But let's create better a List component in order to have routing to the profile page of each hero.

    `components/list/list.js`

        import Cta from 'components/cta/cta';

        function List(props) {
          const { array } = props;

          return (
            <ol>
              {array &&
                array.map((el, i) => (
                  <li>
                    <Cta href={`/heroes/${el}`}>
                      <span>{i}. </span>
                      <span>{el}</span>
                    </Cta>
                  </li>
                ))}
            </ol>
          );
        }

        export default List;

  As you can see we use our component Cta, so we can go to the profile of each Hero, to do that we need dynamic routing.

<span id="#dynamic" >
5. Dynamic routing:

    Let's create a folder inside `pages` called `heroes` and create a js file called `[hero].js`

    `pages/heroes/[hero].js`

        import { useRouter } from "next/router";

        const Hero = () => {
          const router = useRouter();
          const { hero } = router.query;
          return <p>Hero name: {hero}</p>;
        };

        export default Hero;

  Note that we use a module of NextJS called useRouter, with this we can get an instance of the router and get the query
  parameters in the url, in this case the query parameter is what follows after `heroes/` and Next looks if there is a
  js file in the folder `heroes` with parameters in its name (`[hero].js`, that is how `hero` becomes an argument int he query)

<span id="#redux" >
6. Redux:

  I want to present you an example of how using redux and connect the components, to be honest this app is pretty simple to use Redux but this is for academic purposes.

  Before starting let's do it in the simple way, lets send a callback from the `dashboard` page to the `searchBar` in that way the can alter heroes array using the onChange of the `searchBar`

  `components/searchBar/searchBar.js`

        import SvgIcon from "components/svgIcon/svgIcon";
        import css from "./searchBar.scss";

        const handleInputChange = (evt, filterUsingValue) => {
          const inputValue = evt.target.value;
          filterUsingValue && filterUsingValue(inputValue);
        }

        function SearchBar(props) {
          const { placeholder, filterUsingValue } = props;

          return (
            <div className={css.searchBar}>
              <div className={css.searchIcon}>
                <SvgIcon iconName="search" />
              </div>
              <input className={css.searchInput} placeholder={placeholder} onChange={(evt) => handleInputChange(evt, filterUsingValue)}/>
            </div>
          );
        }

        export default SearchBar;

  Note that now SearchBar has a new prop, which is called filterUsingValue and this is just a function of the `dashboard.js`
  file that is sent as prop. Now we can execute that function a pass to is a value, the value of the input.

  `pages/dashboard.js`

        import Cta from "components/cta/cta";
        import SearchBar from "components/searchBar/searchBar";
        import List from "components/list/list";
        import axios from "axios";

        class Dashboard extends React.Component {
          constructor(props) {
            super(props);

            const { heroes } = props;
            this.state = {
              heroes,
              filteredHeroes: heroes
            };
          }

          render() {
            const { filteredHeroes, heroes } = this.state;
            return (
              <div>
                <Cta href="/heroes">Go to heroes list</Cta>
                <h1>Tour of Heroes</h1>
                <SearchBar
                  placeholder="Search a hero"
                  filterUsingValue={value => this.filterHeroes(heroes, value)}
                />
                <List array={filteredHeroes} />
              </div>
            );
          }

          filterHeroes(heroes, value) {
            const pattern = value.toLowerCase();
            this.setState({
              filteredHeroes: heroes.filter(hero =>
                hero.toLowerCase().includes(pattern)
              )
            });
          }
        }

        Dashboard.getInitialProps = async () => {
          const res = await axios.get("http://localhost:3000/static/mocks/heroes.json");
          const heroes = await res.data;
          return { heroes };
        };

        export default Dashboard;

  Note that we convert the page component into a `React.component` in order to use the state of the component and mutate it
  using `this.setState` with the function `filterHeroes`, note that this function is the one that is sent to the `searchBar`,
  so the search is in charge of call this function setting the value of the input.


  Now lets try the same but using Redux.

  To use Redux, we need to do some tricky stuffs, sorry but everything has its cost.


  The first thing we need to understand is that next does not render a React App but miracle, it has by default a file called _app.js where the app is written, we can overload that document creating a file inside `pages` called `_app.js`

    `pages/_app.js`

        import React from 'react'
        import App from 'next/app'

        class MyApp extends App {
          render() {
            const { Component, pageProps } = this.props
            return <Component {...pageProps} />
          }
        }

        export default MyApp

  This is the most basic App component, but we can start to make everything crazy.

  Install the dependencies:

    npm install redux react-redux next-redux-wrapper --save

  Let's first create a folder called `store`, in this folder we will set two folders `actions` and `reducers`,
  in `actions` we will create the regular Redux actions types and actions:

    `store/actions/action-types.js`

        export const CHANGE_SEARCH = 'CHANGE_SEARCH';

    `store/actions/index.js`

        import {
          CHANGE_SEARCH
        } from './action-types';

        export function changeSearch(payload) {
          return { type: CHANGE_SEARCH, payload };
        }

  In `reducers` we will create a Redux reducer to change the state:

    `store/reducers/searchReducer.js`

        import { CHANGE_SEARCH } from '../actions/action-types';

        const initialState = {
          search: ''
        };

        function searchReducer(state = initialState, action) {
          if (action.type === CHANGE_SEARCH) {
            return {
              ...state,
              search: action.payload
            };
          }
          return state;
        }

        export default searchReducer;

  Finally, we will create the store in `store/index.js`

        import { createStore } from 'redux';

        import searchReducer from './reducers/searchReducer';

        // const rootReducer = combineReducers({});

        const makeStore = (initialState, options) => {
          return createStore(searchReducer, initialState);
        };

        export default makeStore;

  Note that makeStore must be a function, because the wrapper we will use it require to create the store in this way.

  Now, we have Redux as we would configure it in Create-React-App.
  Let's modify `_app.js` in order to import the store and set the Provider.

  `pages/_app.js`

        import React from "react";
        import App, { Container } from "next/app";
        import withRedux from "next-redux-wrapper";
        import makeStore from "store/index"
        import {Provider} from "react-redux";


        class MyApp extends App {
          render() {
            const { Component, pageProps, store } = this.props;
            return (
              <Provider store={store}>
                  <Component {...pageProps} />
              </Provider>
            );
          }
        }

        export default withRedux(makeStore)(MyApp);

  Let's add the dispatch in the SearchBar component to give it the ability of change the state.


  `components/searchBar/searchBar`

        import SvgIcon from "components/svgIcon/svgIcon";
        import css from "./searchBar.scss";
        import { connect } from "react-redux";
        import { changeSearch } from "store/actions/index"

        class SearchBar extends React.Component {
          constructor (props) {
            super(props);
            const { dispatch } = props;
            this.updateStoreSearch = (value) => dispatch(changeSearch(value));
          }

          render() {
            const { placeholder } = this.props;
            return (
              <div className={css.searchBar}>
                <div className={css.searchIcon}>
                  <SvgIcon iconName="search" />
                </div>
                <input className={css.searchInput} placeholder={placeholder} onChange={(evt) => this.handleInputChange(evt)}/>
              </div>
            );
          }

          handleInputChange (evt) {
            const inputValue = evt.target.value;
            this.updateStoreSearch(inputValue);
          }
        }

        export default connect(state => state)(SearchBar);

  Note that we change from function component to React.Component to prettify a little bit the code and keep the component as a class. 
  Using connect when we are exporting the component the dispatch function is set in the props of the component.
  That's why in the constructor the dispatch is got from the props. Using dispatch and the action from the `actions`
  we can alter the state.

  Now is time to refactor `pages/dashboard.js`

        import Cta from "components/cta/cta";
        import SearchBar from "components/searchBar/searchBar";
        import List from "components/list/list";
        import axios from "axios";
        import { connect } from "react-redux";

        class Dashboard extends React.Component {
          render() {
            return (
              <div>
                <Cta href="/heroes">Go to heroes list</Cta>
                <h1>Tour of Heroes</h1>
                <SearchBar
                  placeholder="Search a hero"
                />
                <List array={this.filterHeroes()} />
              </div>
            );
          }

          filterHeroes() {
            const { heroes, search } = this.props;
            const pattern = search.toLowerCase();
            return heroes.filter(hero =>
              hero.toLowerCase().includes(pattern)
            );
          }
        }

        Dashboard.getInitialProps = async props => {
          const res = await axios.get("http://localhost:3000/static/mocks/heroes.json");
          const heroes = await res.data;
          return { heroes };
        };

        export default connect(state => state)(Dashboard);

  Note that now we dont need to pass a function to the searchBar component, we have decoupled it.
  Now the state of the reducer is in the property `search` and we can filter the list each time the props are updated
  in the render function.


<span id="#api" >
7. Create an endpoint:

  We will create an endpoint that will request another api to get Hero info:

  The most basic endpoint can be build creating a folder `api` inside `pages`:

  `api/getHeroInfo.js`

        export default (req, res) => {z
          res.setHeader('Content-Type', 'application/json')
          res.statusCode = 200
          res.end(JSON.stringify({ name: 'Nextjs' }))
        }

  Request `http://localhost:3000/api/getHeroInfo`

  To get additional parameters we can get the query from the request:

  `api/getHeroInfo.js`

        export default async (req, res) => {
          const {
            query: { name },
          } = req;
          console.log(name)
          res.setHeader('Content-Type', 'application/json')
          res.statusCode = 200
          res.end(JSON.stringify({ name: 'Nextjs' }))
        }

  Request `http://localhost:3000/api/getHeroInfo?name=Wolverine`

  To get the info of the heroes we will use this api: https://superheroapi.com/

  Log in with your facebook account and then get the ACCESS_TOKEN:

  Create a .env file in the root of the project:

  `.env`

        ACCESS_TOKEN=asdfadgasdg

  `api/getHeroInfo.js`
  Then, we can use axios to get hero info:

        import axios from 'axios';
        require('dotenv').config();

        export default async (req, res) => {
          const {
            query: { name },
          } = req;
          const { ACCESS_TOKEN } = process.env;

          const url = `https://www.superheroapi.com/api.php/${ACCESS_TOKEN}/search/${name}`;
          const response = await axios.get(url);

          res.setHeader('Content-Type', 'application/json')
          res.statusCode = 200
          res.end(JSON.stringify(response.data))
        }


  Request `http://localhost:3000/api/getHeroInfo?name=Wolverine`

