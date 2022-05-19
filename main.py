from flask import Flask, render_template, request, redirect
from app_blockchain.block import _block
from app_blockchain.mine import _mine_block
from app_blockchain import DataB

app = Flask(__name__)
_block()
DataB.update_chain()


@app.route("/blockchain/", methods=['GET'])
@app.route("/blockchain", methods=['GET'])
def AllBlocks():
    DataB.update_chain()
    chains = DataB.chain()
    length = DataB.length_chain()
    return render_template("index.html", len_blocks=length, chains=chains)


@app.route("/blockchain/<index_block>", methods=['GET'])
def OneBlock(index_block):
    chains = DataB.chain()
    this_block = None
    if len(chains) > int(index_block) >= 0:
        this_block = DataB.one_block(int(index_block))
    return render_template("view_block.html", name=index_block, this_block=this_block)


@app.route("/blockchain/<index_block>/data", methods=['GET'])
def DataBlock(index_block):
    chains = DataB.chain()
    this_block = None
    if len(chains) > int(index_block) >= 0:
        this_block = DataB.one_block(int(index_block))["data"]
    return render_template("data_block.html", data_this_block=this_block)


@app.route("/blockchain/mine/", methods=['GET'])
def LengthBlock():
    length = DataB.length_chain()
    return render_template("mine_block.html", len_blocks=length)


@app.route("/blockchain/mine/mining", methods=['POST'])
def MineBlock():
    if request.form["mine_block"] == "Mine" and 100 > DataB.length_chain() >= 0:
        data = request.form.get("data_from_block")
        _mine_block(data_block=data)
        DataB.update_chain()
        return redirect("/blockchain/mine/", code=302)


@app.route("/blockchain/mine/delete", methods=['POST'])
def DeleteChain():
    if request.form["delete_chain"] == "Del" and DataB.length_chain() > 0:
        DataB.delete_all()
        _block()
        DataB.update_chain()
        return redirect("/blockchain/mine/", code=302)


if __name__ == "__main__":
    print("http://127.0.0.1:8000/blockchain")
    print("http://127.0.0.1:8000/blockchain/mine/")
    app.run(port=8000)
