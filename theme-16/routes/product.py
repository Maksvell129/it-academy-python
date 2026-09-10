from flask import Blueprint, request

products_blueprint = Blueprint("products", __name__)


@products_blueprint.route("/<int:product_id>")
def product(product_id):
    return f"Product: {product_id}"

@products_blueprint.route("")
def products():
    category = request.args.get("category")
    page = request.args.get("page")

    return f"Category: {category} - Page: {page} - Other: {", ".join(set(request.args.keys() - set(["category", "page"])))}"

