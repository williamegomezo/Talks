function SvgIcon(props) {
  const { iconName } = props;
  const Icon = require(`static/icons/${iconName}.svg`);
  return <Icon />;
}

export default SvgIcon;