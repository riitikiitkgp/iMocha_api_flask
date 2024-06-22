@app.route('/reports/<int:test_invitation_id>/pdf', methods=['GET'])
def export_pdf_report(test_invitation_id):
    pdf_report_url = f"https://apiv3.imocha.io/v3/reports/{test_invitation_id}/pdf"
    response = {
        "pdfReport": pdf_report_url
    }

    return jsonify(response)
