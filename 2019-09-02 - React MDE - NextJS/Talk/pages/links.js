import Link from "next/link";
import Button from '@material-ui/core/Button';


const renderLinks = () => {
  const names = ["William", "Manuel", "Carlos"];
  return names.map(name => (
    <Link href="/users/[name]" as={`/users/${name}`}>
      <Button className="demo-button" variant="contained" color="primary">Go to {name}</Button>
    </Link>
  ));
};

function Links() {
  return <div>
    {renderLinks()}
    <style global jsx>{`
          div {
            display: flex;
            flex-direction: column;
          }
          .demo-button {
            margin: 20px;
            width: 200px;
          }
        `}
    </style>
  </div>;
}

export default Links;
