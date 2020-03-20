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
