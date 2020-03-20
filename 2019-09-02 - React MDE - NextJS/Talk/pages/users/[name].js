import { useRouter } from 'next/router';
import axios from 'axios';

const User = (props) => {
  console.log(props)
  const router = useRouter();
  const { name } = router.query;

  return <div>
    <p>User: {name}</p>
    <p>Gender: {props.gender}</p>
  </div>;
};

User.getInitialProps = async (ctx) => {
  const name = ctx.query.name;
  const res = await axios.get(`https://gender-api.com/get?name=${name}&key=wAZCHlLqwPdltSdamG`)
  return res.data;
}

export default User;