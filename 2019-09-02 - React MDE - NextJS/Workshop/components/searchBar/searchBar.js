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
