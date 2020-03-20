import Link from 'next/link';
import css from './image.scss'

function MyImage() {
  return (
    <Link href="/" as="/fake">
      <img className={css.image} src="/static/next.png" alt="my image" />
    </Link>);
}

export default MyImage;