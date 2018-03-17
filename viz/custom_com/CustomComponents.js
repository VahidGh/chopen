class LineGraph extends Component {
    constructor() {
        super();
        this.plot = this.plot.bind(this);
    }
    plot(props) {
        LineGraph(
            props.id,
            props.xData,
            props.yData,
            props.xTitle,
            props.yTitle,
            props.color
        );
    }

    componentDidMount() {
        this.plot(this.props);
    }

    componentWillReceiveProps(newProps) {
        this.plot(newProps);
    }

    render() {
        return <div id={props.id}/>
    }
}

LineGraph.propTypes = {
    id: PropTypes.string,
    xData: PropTypes.array,
    yData: PropTypes.array,
    xTitle: PropTypes.array,
    color: PropTypes.string
}
