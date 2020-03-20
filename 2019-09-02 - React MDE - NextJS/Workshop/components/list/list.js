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
