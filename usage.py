import dash
import dash_html_components as html
import feffery_antd_components as fac

app = dash.Dash(__name__)

app.layout = html.Div(
    html.Div(
        fac.AntdDatePicker(
            picker='year',
            placeholder='请选择年份',
            defaultPickerValue={
                'value': '2020',
                'format': 'YYYY'
            }
        )
    ),
    style={
        'height': '10000px',
        'paddingTop': '500px',
        'display': 'flex'
    }
)

if __name__ == '__main__':
    app.run_server(debug=True, port=8000)
