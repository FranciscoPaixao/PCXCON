from pcxcon import *
from flask import Flask, request
from flask_restx import Resource, Api, fields


app = Flask(__name__)
api = Api(app)

@api.route('/api/uso/<string:usoPrincipal>')
class uso_principal(Resource):
    @api.doc(params={'usoPrincipal': 'Aceita: Escritorio, Programacao, Jogos, Modelagem3D, CompilacaoEVideoEncoding'})
    def get(self, usoPrincipal):
        resultado = inferencia.map_query(['cpu','gpu','ram', 'monitor','armazenamento', 'mouse', 'teclado', 'perifericoadicional'],evidence={'usoprincipal' : usoPrincipal})
        return resultado


@api.route('/api/acharCategoria')
class acharCategoria(Resource):
    @api.doc(params={
        'cpu': 'Aceita: Ryzen3, Ryzen5, Ryzen7, RyzenThreadripper',
        'gpu': 'Aceita: GPUIntegrada, RTX3050, RTX3060, RTX3070, RTX3080, RTX3090',
        'ram': 'Aceita: RAM8GB, RAM16GB, RAM32GB, RAM64GB, RAM128GB',
        'armazenamento': 'Aceita: SSD512GB, SSD1TB, HDD1TB, HDD4TB',
        'teclado': 'Aceita: Mecanico, Membrana',
        'mouse': 'Aceita: MousePadaria, Top5DeluxM800PRO, Top4MotospeedDarmosharkM3, Top3AjazzAj139, Top2KysonaM600, Top1DragonFlyVgnF1',
        'monitor': 'Aceita: QHD240HzIPS, FHD60hzTN, UHD60hzIPSFoscaC1000P1, UHD60hzIPSBrilhosaC1000P1',
        'perifericoAdicional': 'Aceita: MesaDigitalizadora, SemPeriferico'
    })
    def get(self):
        arrayParametros = {}
        arrayParametros['cpu'] = request.args.get('cpu','')
        arrayParametros['gpu'] = request.args.get('gpu','')
        arrayParametros['ram'] = request.args.get('ram','')
        arrayParametros['armazenamento'] = request.args.get('armazenamento','')
        arrayParametros['teclado'] = request.args.get('teclado','')
        arrayParametros['mouse'] = request.args.get('mouse','')
        arrayParametros['monitor'] = request.args.get('monitor','')
        arrayParametros['perifericoAdicional'] = request.args.get('perifericoadicional','')

        arrayParametros = {chave: valor for chave, valor in arrayParametros.items() if valor.strip() != ''}

        if(len(arrayParametros) < 1):
            return '{"Erro": "Parametros invalidos"'
        
        resultado = inferencia.map_query(['usoprincipal'],evidence=arrayParametros)

        return resultado

if __name__ == '__main':
    app.run(debug=False, Host="0.0.0.0")
