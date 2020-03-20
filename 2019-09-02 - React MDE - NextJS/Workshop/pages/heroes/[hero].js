import { useRouter } from "next/router";

const Hero = () => {
  const router = useRouter();
  const { hero } = router.query;
  return <p>Hero name: {hero}</p>;
};

export default Hero;
