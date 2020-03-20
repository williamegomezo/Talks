import _ from "lodash";
import Head from "next/head";
import Button from '@material-ui/core/Button';

// Loading solution: https://github.com/mui-org/material-ui/tree/master/examples/nextjs
function Loading() {
  return (
    <div>
      <Head>
        <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap" />
      </Head>
      <Button variant="contained" color="primary">
        Hello World
      </Button>
    </div>
  );
}

export default Loading;
